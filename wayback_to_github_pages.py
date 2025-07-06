#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Wayback MachineからダウンロードしたHTMLファイルをGitHub Pages用に変換するスクリプト
link.pyのコメントに基づいて作成
"""

import os
import re
import shutil
from pathlib import Path
from urllib.parse import unquote
import html

class WaybackToGitHubPagesConverter:
    def __init__(self, root_dir="dvorakj"):
        self.root_dir = Path(root_dir)
        self.processed_files = set()
        
        # Wayback Machine関連のパターン
        self.wayback_patterns = [
            # Wayback Machine URLパターン
            r'https://web\.archive\.org/web/\d+(?:mp_)?/(?:https?://)?',
            # Wayback Machine ツールバー関連
            r'<!-- BEGIN WAYBACK TOOLBAR INSERT -->.*?<!-- END WAYBACK TOOLBAR INSERT -->',
            # Wayback Machine スクリプト
            r'<script[^>]*>.*?__wm\..*?</script>',
            # Wayback Machine CSS/JS
            r'<link[^>]*banner-styles\.css[^>]*>',
            r'<link[^>]*iconochive\.css[^>]*>',
            r'<script[^>]*(?:athena|bundle-playback|wombat|ruffle)\.js[^>]*>.*?</script>',
            # Wayback Machine コメント
            r'<!-- saved from url=.*?-->',
            # Wayback Machine toolbar関連要素
            r'<div[^>]*id="wm-.*?</div>',
            r'<template[^>]*>.*?</template>',
            # Wayback Machine印刷用
            r'<div[^>]*id="wm-ipp-print".*?</div>',
        ]
        
        # CGI関連のパターン
        self.cgi_patterns = [
            # CGIフォーム
            r'<form[^>]*action="[^"]*wiliki\.cgi[^"]*"[^>]*>.*?</form>',
            # CGIリンク（検索機能など）
            r'<link[^>]*href="[^"]*wiliki\.cgi[^"]*"[^>]*>',
        ]

    def clean_filename(self, filename):
        """ファイル名から不要な文字を削除"""
        # .ダウンロード を削除
        filename = re.sub(r'\.ダウンロード$', '', filename)
        # その他の不要な文字を削除
        filename = re.sub(r'[<>:"|?*]', '', filename)
        return filename

    def convert_wayback_url_to_local(self, url):
        """Wayback Machine URLをローカルパスに変換"""
        if not url:
            return url
            
        # 外部リンクの場合はそのまま返す
        if url.startswith(('http://', 'https://')) and 'blechmusik.xii.jp' not in url and 'web.archive.org' not in url:
            return url
            
        # Wayback Machine URLを削除
        for pattern in [
            r'https://web\.archive\.org/web/\d+(?:mp_)?/',
            r'https://web\.archive\.org/web/\d+/'
        ]:
            url = re.sub(pattern, '', url)
        
        # blechmusik.xii.jp/dvorakj/ を削除
        url = re.sub(r'https?://blechmusik\.xii\.jp/dvorakj/', '', url)
        
        # wiliki.cgi パラメータを変換
        if 'wiliki.cgi' in url:
            # クエリパラメータを解析してファイル名に変換
            if '?' in url:
                query = url.split('?')[1]
                # URLデコード
                query = unquote(query)
                query = html.unescape(query)
                
                # パラメータを解析
                if query.startswith('DvorakJ'):
                    # DvorakJ:全般 → DvorakJ_全般.html
                    filename = query.replace(':', '_') + '.html'
                    return filename
                elif 'c=s&key=' in query:
                    # 検索ページ - とりあえず元のページに戻す
                    key = query.split('key=')[1].replace('[[', '').replace(']]', '')
                    key = unquote(key)
                    if key == 'DvorakJ':
                        return 'DvorakJ.html'
                    else:
                        filename = key.replace(':', '_') + '.html'
                        return filename
            else:
                # wiliki.cgi のみの場合はインデックスページ
                return 'DvorakJ.html'
        
        # .ダウンロード を削除
        url = self.clean_filename(url)
        
        # 相対パスの調整
        if url.startswith('./'):
            url = url[2:]
        
        return url

    def remove_wayback_elements(self, content):
        """Wayback Machine関連の要素を削除"""
        # 複数行にまたがる要素を削除
        content = re.sub(
            r'<!-- BEGIN WAYBACK TOOLBAR INSERT -->.*?<!-- END WAYBACK TOOLBAR INSERT -->',
            '',
            content,
            flags=re.DOTALL
        )
        
        # ツールバー関連のdivを削除
        content = re.sub(
            r'<div[^>]*(?:id="wm-|class="[^"]*wb-)[^>]*>.*?</div>',
            '',
            content,
            flags=re.DOTALL
        )
        
        # テンプレート要素を削除
        content = re.sub(
            r'<template[^>]*>.*?</template>',
            '',
            content,
            flags=re.DOTALL
        )
        
        # Wayback Machine スクリプトを削除
        content = re.sub(
            r'<script[^>]*(?:athena|bundle-playback|wombat|ruffle)\.js[^>]*>.*?</script>',
            '',
            content,
            flags=re.DOTALL
        )
        
        # その他のWayback Machine関連要素
        for pattern in [
            r'<!-- saved from url=.*?-->',
            r'<script[^>]*>.*?archive_analytics.*?</script>',
            r'<script[^>]*>.*?__wm\..*?</script>',
            r'<link[^>]*(?:banner-styles|iconochive)\.css[^>]*>',
            r'<div[^>]*id="wm-ipp-print".*?</div>',
            r'style="--wm-toolbar-height: [^"]*"',
            r'<div class="wb-autocomplete-suggestions[^>]*></div>',
        ]:
            content = re.sub(pattern, '', content, flags=re.DOTALL)
        
        return content

    def remove_cgi_elements(self, content):
        """CGI関連の要素を削除または変換"""
        # CGIフォームを削除
        content = re.sub(
            r'<form[^>]*action="[^"]*wiliki\.cgi[^"]*"[^>]*>.*?</form>',
            '',
            content,
            flags=re.DOTALL
        )
        
        # CGI関連のリンクを削除
        content = re.sub(
            r'<link[^>]*href="[^"]*wiliki\.cgi[^"]*"[^>]*>',
            '',
            content
        )
        
        # wiliki_tools divを削除
        content = re.sub(
            r'<div[^>]*id="wiliki_tools"[^>]*>.*?</div>',
            '',
            content,
            flags=re.DOTALL
        )
        
        return content

    def convert_links_in_content(self, content):
        """コンテンツ内のリンクを変換"""
        def replace_link(match):
            href = match.group(1)
            new_href = self.convert_wayback_url_to_local(href)
            return f'href="{new_href}"'
        
        # href属性を変換
        content = re.sub(r'href="([^"]*)"', replace_link, content)
        
        # src属性も変換
        def replace_src(match):
            src = match.group(1)
            new_src = self.convert_wayback_url_to_local(src)
            return f'src="{new_src}"'
        
        content = re.sub(r'src="([^"]*)"', replace_src, content)
        
        return content

    def clean_html_content(self, content):
        """HTMLの不要な部分を削除し、見た目と内容に関する部分のみを残す"""
        # 最初にWayback Machine関連を削除
        content = self.remove_wayback_elements(content)
        
        # CGI関連を削除
        content = self.remove_cgi_elements(content)
        
        # リンクを変換
        content = self.convert_links_in_content(content)
        
        # 空白行を整理
        content = re.sub(r'\n\s*\n\s*\n', '\n\n', content)
        
        return content

    def process_html_file(self, file_path):
        """単一のHTMLファイルを処理"""
        print(f"Processing: {file_path}")
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
        except UnicodeDecodeError:
            # Shift_JISやその他のエンコーディングを試す
            for encoding in ['shift_jis', 'cp932', 'iso-2022-jp']:
                try:
                    with open(file_path, 'r', encoding=encoding) as f:
                        content = f.read()
                    break
                except UnicodeDecodeError:
                    continue
            else:
                print(f"  Error: Could not decode {file_path}")
                return False
        
        # HTMLを清理
        cleaned_content = self.clean_html_content(content)
        
        # ファイルを上書き
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(cleaned_content)
        
        print(f"  Cleaned: {file_path}")
        return True

    def rename_files_and_directories(self):
        """ファイルとディレクトリの名前を変更"""
        # まず、ファイルの名前を変更
        for root, dirs, files in os.walk(self.root_dir):
            for file in files:
                if '.ダウンロード' in file:
                    old_path = Path(root) / file
                    new_name = self.clean_filename(file)
                    new_path = Path(root) / new_name
                    
                    if old_path != new_path:
                        print(f"Renaming file: {old_path} -> {new_path}")
                        old_path.rename(new_path)
        
        # ディレクトリの名前を変更（深い階層から）
        for root, dirs, files in os.walk(self.root_dir, topdown=False):
            for dir_name in dirs:
                if '.ダウンロード' in dir_name or '_files' in dir_name:
                    old_path = Path(root) / dir_name
                    new_name = self.clean_filename(dir_name)
                    new_path = Path(root) / new_name
                    
                    if old_path != new_path and not new_path.exists():
                        print(f"Renaming directory: {old_path} -> {new_path}")
                        old_path.rename(new_path)

    def process_all_files(self):
        """すべてのHTMLファイルを再帰的に処理"""
        if not self.root_dir.exists():
            print(f"Error: Directory {self.root_dir} does not exist")
            return
        
        print(f"Starting conversion in directory: {self.root_dir}")
        
        # まずファイル名を変更
        print("Step 1: Renaming files and directories...")
        self.rename_files_and_directories()
        
        # HTMLファイルを処理
        print("Step 2: Processing HTML files...")
        html_files = list(self.root_dir.rglob("*.html"))
        
        for html_file in html_files:
            if html_file not in self.processed_files:
                self.process_html_file(html_file)
                self.processed_files.add(html_file)
        
        print(f"Conversion completed! Processed {len(self.processed_files)} HTML files.")

    def create_index_html(self):
        """メインのindex.htmlを作成"""
        index_content = """<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>DvorakJ Documentation</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 40px; line-height: 1.6; }
        h1 { color: #333; }
        ul { list-style-type: none; padding: 0; }
        li { margin: 10px 0; }
        a { color: #0066cc; text-decoration: none; }
        a:hover { text-decoration: underline; }
        .section { margin: 20px 0; border-left: 3px solid #0066cc; padding-left: 20px; }
    </style>
</head>
<body>
    <h1>DvorakJ Documentation</h1>
    
    <div class="section">
        <h2>Main Page</h2>
        <ul>
            <li><a href="DvorakJ.html">DvorakJ</a></li>
        </ul>
    </div>
    
    <div class="section">
        <h2>General Information</h2>
        <ul>
            <li><a href="DvorakJ_全般.html">DvorakJ:全般</a></li>
            <li><a href="DvorakJ_全般_概要.html">DvorakJ:全般:概要</a></li>
            <li><a href="DvorakJ_全般_動作環境.html">DvorakJ:全般:動作環境</a></li>
            <li><a href="DvorakJ_全般_ライセンス.html">DvorakJ:全般:ライセンス</a></li>
        </ul>
    </div>
    
    <div class="section">
        <h2>Tutorial</h2>
        <ul>
            <li><a href="DvorakJ_チュートリアル.html">DvorakJ:チュートリアル</a></li>
            <li><a href="DvorakJ_チュートリアル_日本語入力用配列を変更する.html">日本語入力用配列を変更する</a></li>
            <li><a href="DvorakJ_チュートリアル_ショートカットキーの挙動を変更する.html">ショートカットキーの挙動を変更する</a></li>
            <li><a href="DvorakJ_チュートリアル_マウスの挙動を変更する.html">マウスの挙動を変更する</a></li>
        </ul>
    </div>
    
    <div class="section">
        <h2>Reference Manual</h2>
        <ul>
            <li><a href="DvorakJ_レファレンスマニュアル.html">DvorakJ:レファレンスマニュアル</a></li>
            <li><a href="DvorakJ_レファレンスマニュアル_キーボード.html">キーボード</a></li>
            <li><a href="DvorakJ_レファレンスマニュアル_キー配列.html">キー配列</a></li>
            <li><a href="DvorakJ_レファレンスマニュアル_FAQ.html">FAQ</a></li>
        </ul>
    </div>
</body>
</html>"""
        
        index_path = self.root_dir / "index.html"
        with open(index_path, 'w', encoding='utf-8') as f:
            f.write(index_content)
        
        print(f"Created index.html at {index_path}")


def main():
    """メイン関数"""
    converter = WaybackToGitHubPagesConverter()
    
    # 全ファイルを処理
    converter.process_all_files()
    
    # インデックスページを作成
    converter.create_index_html()
    
    print("\n=== Conversion Summary ===")
    print("✓ Removed Wayback Machine toolbar and scripts")
    print("✓ Removed CGI forms and functionality")
    print("✓ Converted internal links to relative paths")
    print("✓ Cleaned up file names (removed .ダウンロード)")
    print("✓ Created index.html for GitHub Pages")
    print("\nYour site is now ready for GitHub Pages!")


if __name__ == "__main__":
    main()
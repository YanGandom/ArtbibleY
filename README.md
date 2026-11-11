# Project Y 美术制作手册

Project Y 的美术制作、跨工种交接、资源集成与验收手册。橙色文字表示待确认、待补充或待制定内容。

## 查看

双击 `index.html` 即可离线阅读，无需安装依赖。支持章节导航和全文搜索。页面用于阅读，正文通过修改 HTML 源文件维护。

## 上传 GitHub

1. 解压发布 ZIP，将其中的文件上传到仓库根目录。不要仅上传 ZIP，否则不能直接作为网页浏览。
2. 如果要通过网页访问，在仓库 **Settings → Pages → Build and deployment** 选择 **Deploy from a branch**，选择保存文件的分支和 **/ (root)**，保存。
3. 发布完成后使用 GitHub Pages 显示的网址访问。此项目为纯静态 HTML，无需构建。

仓库及 Pages 的可见性请按团队需要设置；不要默认认为私有仓库对应的 Pages 站点也一定私有。

## 修改和保存

- `index.html` 是唯一正式正文源文件，直接修改它即可。
- 页面已移除编辑、打印和下载按钮。请在编辑器中修改 `index.html`，或让 Codex 修改；完成后重新打包。
- 页面没有云端同步功能，也不会直接写入 GitHub。上传新版文件并提交后，Pages 才会更新。
- 大幅调整章节、表格或交互时，可让 Codex 修改 `index.html`。

## 生成最新版上传包

Windows 双击 `package.cmd`，或在安装 Python 3 的环境中运行：

```sh
python package_release.py
```

脚本读取同目录的最新 `index.html`，在 `releases/` 下生成带时间戳的 ZIP，以及方便查找的 `ProjectY-Art-Handbook-latest.zip`。已有时间戳版本保留。

发布包只包含正文、说明、打包工具和发布信息；不包含历史备份、测试文件、截图或原 Word 文档。上传更新时，以解压后的文件覆盖仓库中的对应文件，再提交变更；无需将 `releases/` 上传。

`release.json` 记录打包时间、正文版本和 SHA-256 校验值。打包不会自动提高正文版本号；内容有正式修订时，请同步更新封面和修订记录。

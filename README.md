# SHICTHRS ENCR System

[![License: GPL-3.0](https://img.shields.io/badge/License-GPL--3.0-blue.svg)](https://opensource.org/licenses/GPL-3.0)
[![Python Version](https://img.shields.io/badge/python-3.6%2B-blue.svg)](https://www.python.org/downloads/)

SHICTHRS ENCR 是一个轻量级 Python 加密与验证工具库，提供了一系列实用的加密、哈希和身份验证功能。

## 功能特性

- **哈希计算**：支持 MD5 哈希值计算，包括文本和文件哈希
- **Base64 编解码**：提供 Base64 加密和解密功能
- **身份验证**：支持中国身份证号码验证
- **文本检测**：支持中文文本检测功能
- **异常处理**：完善的异常处理机制，便于调试

## 安装方法

### 从源码安装

```bash
git clone https://github.com/JNTMTMTM/SHICTHRS_ENCR.git
cd SHICTHRS_ENCR
pip install -e SHICTHRSENCR/
```

### 使用 pip 安装

```bash
pip install SHICTHRSENCR
```

## 使用示例

```python
from SHICTHRSENCR import *

# 计算文本的 MD5 哈希值
hash_code = SHRENCR_get_hash_code("Hello World")
print(f"MD5 Hash: {hash_code}")

# 计算文件的 MD5 哈希值
file_hash = SHRENCR_get_file_hash_code("path/to/your/file.txt")
print(f"File MD5: {file_hash}")

# 获取哈希掩码
hash_mask = SHRENCR_get_hash_code_mask("example")
print(f"Hash Mask: {hash_mask}")

# Base64 加密
encrypted = SHRENCR_en_base64_code("Hello World")
print(f"Base64 Encrypted: {encrypted}")

# Base64 解密
decrypted = SHRENCR_de_base64_code(encrypted)
print(f"Base64 Decrypted: {decrypted}")

# 验证中国身份证号码
is_valid_id = SHRENCR_check_identity_number("11010519491231002X")
print(f"ID Number Valid: {is_valid_id}")

# 检查是否为中文文本
is_chinese = SHRENCR_check_chinese_text("你好，世界！")
print(f"Is Chinese Text: {is_chinese}")
```

## API 文档

### 哈希计算

- `SHRENCR_get_hash_code(org_code: str) -> str`
  - 计算文本的 MD5 哈希值
  
- `SHRENCR_get_file_hash_code(path: str) -> str`
  - 计算文件的 MD5 哈希值
  - 如果路径不存在或不是文件，会抛出异常
  
- `SHRENCR_get_hash_code_mask(org_code: str) -> str`
  - 获取哈希掩码

### Base64 编解码

- `SHRENCR_en_base64_code(org_code: str) -> str`
  - 将文本进行 Base64 编码
  
- `SHRENCR_de_base64_code(en_code: str) -> str`
  - 将 Base64 编码的文本解码

### 验证与检测

- `SHRENCR_check_identity_number(identity_number: str) -> bool`
  - 验证中国身份证号码的有效性（支持15位和18位）
  
- `SHRENCR_check_chinese_text(text: str) -> bool`
  - 检查文本是否为中文

### 异常处理

库提供了 `SHRENCRException` 异常类，所有函数在遇到错误时会抛出此异常，包含详细的错误信息。

## 依赖

- Python 3.6+
- colorama==0.4.6

## 许可证

本项目采用 [GPL-3.0](LICENSE) 许可证。

## 作者

- 作者: SHICTHRS-JNTMTMTM
- 邮箱: contact@shicthrs.com
- GitHub: https://github.com/JNTMTMTM/SHICTHRS_ENCR

## 版权

Copyright © 2025-2026 SHICTHRS, Std. All rights reserved.

## 贡献

欢迎提交 Issue 和 Pull Request 来帮助改进此项目。

> Algorithms = rule ; Questioning = approval
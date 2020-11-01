# Simplelayout-CLI Project

> 编写包含命令行接口的简单布局生成器，生成给定分辨率、给定组件大小、给定组件位置的布局方案，以数据格式、图片形式存储，保存到指定目录。

## Homework 1

### 简介

**命令行接口**（**C**ommand-**L**ine **I**nterface）是一种通过命令文本的输入、非图形化的方式进行交互的高效手段。虽然同学们在日常操作软件的过程中以图形化界面（GUI）为主，但 CLI 的使用与编写同样是不可或缺的必备技能。 

CLI 的编写是以命令行的解析为基础的，虽然可以自己实现解析器，但 Python 中已经提供了标准模块 [argparse](https://docs.python.org/zh-cn/3/howto/argparse.html) 来负责这部分工作，学会该模块的基本用法就能实现复杂的 CLI 逻辑，包括子命令、参数类型限制、说明文档等。


### 作业要求

本次作业将编写 simplelayout 的命令行解析部分，基本要求是：

1. 在 simplelayout.py 中完成 `main()` 函数的编写，实现命令行解析功能。
1. **无需实现数据生成部分**
1. 通过单元测试，根据功能点获得相应分数。

**接口示例：**

```bash
python simplelayout.py --board_grid 100 --unit_grid 10 --unit_n 3 --positions 1 15 33 --outdir dir1/dir2 --file_name example
```

**参数：**

- `--board_grid`:  int，布局板分辨率，代表矩形区域的边长像素数
- `--unit_grid`: int，矩形组件分辨率；**要求** `board_grid` 能整除 `unit_grid`，若不满足退出程序
- `--unit_n`: int，组件数
- `--positions`: 每个元素是 int，数量与 `unit_n` 一致；代表每个组件的位置编号，位置为从1开始的整数，上限为 `(board_grid/unit_grid)^2` ，若不满足要求退出程序
- `-o 或者 --outdir`: str，输出结果的目录，默认为当前目录下的 `example_dir` 目录；若目录不存在程序会自行创建，支持跨平台路径
- `--file_name`: str，输出文件名（不包括文件类型后缀），默认为 `example`

**输出要求：**

- 按命令行指令在 `outdir` 下生成 `file_name.mat` 和 `file_name.jpg` 两个文件，这次作业生成两个**空文件**即可 ，**仅需路径与文件名正确即可**。

**评分要点：**

采用自动化测试实现自动评分

|                    要点                    | 分值 |
| :----------------------------------------: | :--: |
|                  代码规范                  |  1   |
|      实现命令行解析，通过正确示例测试      |  3   |
|            board_grid 参数设置             |  1   |
|             unit_grid 参数设置             |  1   |
|              unit_n 参数设置               |  1   |
|            poisitions 参数设置             |  1   |
| outdir 与 file_name 参数设置，正确生成文件 |  2   |
|                  **总分**                  |  10  |


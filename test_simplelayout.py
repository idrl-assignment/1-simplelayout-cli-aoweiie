import sys

import pytest

import simplelayout


def run_simplelayout(
    board_grid=10,
    unit_grid=2,
    unit_n=2,
    positions="1 4",
    outdir="dir1/dir2",
    file_name="example",
):
    cmd = (
        f"simplelayout.py --board_grid {board_grid} "
        f"--unit_grid {unit_grid} "
        f"--unit_n {unit_n} "
        f"--positions {positions} "
        f"--outdir {str(outdir)} "
        f"--file_name {file_name}"
    )
    sys.argv = cmd.split()
    simplelayout.main()


def test_cli_ok(tmp_path):
    run_simplelayout(outdir=tmp_path)


def test_cli_board_grid(tmp_path):
    with pytest.raises(SystemExit):
        run_simplelayout(board_grid=10.1, outdir=tmp_path)


def test_cli_unit_grid(tmp_path):
    with pytest.raises(SystemExit):
        run_simplelayout(unit_grid=2.1, outdir=tmp_path / "1")

    with pytest.raises(SystemExit):
        run_simplelayout(board_grid=10, unit_grid=3, outdir=tmp_path / "2")


def test_cli_unit_n(tmp_path):
    with pytest.raises(SystemExit):
        run_simplelayout(unit_n=3.1, outdir=tmp_path)


def test_cli_postitions(tmp_path):
    with pytest.raises(SystemExit):
        run_simplelayout(positions="1.1", outdir=tmp_path / "1")
    with pytest.raises(SystemExit):
        run_simplelayout(
            unit_n=2, positions="1 2 3", outdir=tmp_path / "2"
        )  # 组件数与位置不一致


def test_outdir(tmp_path):
    outpath = tmp_path / "dir1/dir2"
    file_name = "example"
    run_simplelayout(outdir=str(outpath), file_name=file_name)
    file_mat = outpath / f"{file_name}.mat"
    file_jpg = outpath / f"{file_name}.jpg"
    assert file_mat.exists(), "mat 文件不存在！"
    assert file_jpg.exists(), "jpg 文件不存在！"

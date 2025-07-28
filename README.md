# zm01

Small commands that make my life better.

## Tools

### Train service information

```
zm train
+------------------+----------+--------------------------------------------------+
| 路線名      | 情報種別       | URL                                              |
+------------------+----------+--------------------------------------------------+
| 南海高野線   | 運行情報     | https://transit.yahoo.co.jp/diainfo/346/0          |
| 阪和線       | 運行情報     | https://transit.yahoo.co.jp/diainfo/274/0          |
| 大阪環状線   | 運行情報     | https://transit.yahoo.co.jp/diainfo/263/0          |
| 御堂筋線     | 運行情報     | https://transit.yahoo.co.jp/diainfo/321/0          |
+------------------+----------+--------------------------------------------------+
```
## install

## Try without really installing it

```
uvx git+https://github.com/haruka-1112/zm01 train
```

### Ready to install?

Install ot woth uv
uv tool install git+https://github.com/haruka-1112/zm01 --reinstall
or with pipx
### Uninstall

```
uv tool uninstool zm01
```

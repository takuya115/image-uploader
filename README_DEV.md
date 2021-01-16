# サーバー
## インストール
```bash
$ pipenv sync --dev
```

## uvicornの起動
```bash
$ uvicorn --app-dir server main:app --reload
# または
$ cd server
$ uvicorn main:app --reload
```
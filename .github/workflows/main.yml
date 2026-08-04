name: Auto Publish GameMonetize to Blogger

on:
  workflow_dispatch:
  # schedule:
  #   - cron: '0 */6 * x *' # اختياري للتشغيل التلقائي كل 6 ساعات

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      # 1. سحب الكود من المستودع
      - name: Checkout repository
        uses: actions/checkout@v3

      # 2. إعداد بايثون
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'

      # 3. تثبيت المكتبات اللازمة للاتصال وبلوجر
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install requests google-auth google-auth-oauthlib google-api-python-client

      # 4. تشغيل ملف السكريبت مع تمرير الأسرار (Secrets)
      - name: Run publisher script
        env:
          BLOG_ID: ${{ secrets.BLOG_ID }}
          CLIENT_ID: ${{ secrets.CLIENT_ID }}
          CLIENT_SECRET: ${{ secrets.CLIENT_SECRET }}
          REFRESH_TOKEN: ${{ secrets.REFRESH_TOKEN }}
        run: |
          python main.py

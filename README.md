# チョイソコひの 利用状況ダッシュボード（プロトタイプ）

滋賀県日野町のデマンド型乗合交通**「チョイソコひの」**の公開運行レポート（PDF）からデータを抽出し、視覚的にわかりやすく閲覧できるよう構築した、オープンデータ利活用のための実証実験プロジェクトです。

ブラウザ上で完結する SPA（シングルページアプリケーション）で、外部ビルド不要・`index.html` を開くだけで動作します。デジタル庁「ダッシュボードデザインガイドブック」の考え方を参考に、認知負荷の低い UI を意識しています。

👉 **公開URL:** `https://kken78.github.io/choisoko-hino-dashboard/`

## 🚀 主な特徴

1. **「累計4時点」を切り替えられる構成**
   チョイソコひのの運行レポートは、運行開始（令和5年3月）からの**累計**で発行されています。本ダッシュボードは R5.3（初月）／ R6.3（1年）／ R7.3（2年）／ R8.3（3年）の4時点を上部のタブで切り替え、登録・利用会員数や年代構成などのスナップショットを比較できます。

2. **利用の伸びが一目でわかる月別推移**
   利用件数・1日当たり件数・月別利用人数を、運行開始からの全月で連続表示します。令和5年9月の**無償→有償運行**への移行も明示しています。

3. **「誰が・いつ・どこへ」を分解**
   年代別・男女別の会員構成、時間帯・曜日・予約タイミング・予約方法、目的地停留所の乗降回数（上位15）、地区別利用状況（全32地区＋その他）を収録。通院・買い物の午前中に利用が集中し、80歳代以上・女性に厚い、といった地域の足の実像が読み取れます。

4. **外部サイトへの埋め込み対応**
   URL末尾に `?embed=true` を付けるとヘッダー・フッターが非表示になり、`#trend` などのハッシュで開く位置も指定できます。

   ```html
   <iframe
       src="https://kken78.github.io/choisoko-hino-dashboard/?embed=true#trend"
       width="100%" height="520" style="border:none;background:transparent;">
   </iframe>
   ```

5. **モバイル・アクセシビリティ対応**
   スマートフォンでは1列レイアウト。キーボードフォーカス表示、`prefers-reduced-motion` にも配慮しています。

## 📊 収録データ（`data/`）

| ファイル | 内容 |
| --- | --- |
| `summary.csv` | 4時点の累計サマリー（登録・利用会員数、利用件数、利用人数、乗合率、男女比、予約方法比、路線数） |
| `monthly.csv` | 月別の利用件数・1日当たり件数・月別利用人数（運行開始〜R8.3、運行区分付き） |
| `age.csv` | 年代別構成（登録／利用、各時点、％） |
| `hourly.csv` | 時間帯別利用割合（％） |
| `weekday.csv` | 曜日別 1日あたり平均利用件数 |
| `booking_timing.csv` | 予約時期割合（％） |
| `booking_method.csv` | 予約方法割合（WEB／電話、％） |
| `stops.csv` | 目的地停留所 乗降回数 上位15（R8.3累計） |
| `district.csv` | 地区別利用状況（R8.3累計） |

**出典:** 日野町公式サイト「[チョイソコひの](https://www.town.shiga-hino.lg.jp/0000006854.html)」で公開されている利用状況レポート（PDF）

- [利用状況 令和5年3月末まで](https://www.town.shiga-hino.lg.jp/cmsfiles/contents/0000006/6854/riyoujyoukyouR5.3.pdf)
- [利用状況 令和6年3月末まで](https://www.town.shiga-hino.lg.jp/cmsfiles/contents/0000006/6854/riyoujyoukyouR6.3.pdf)
- [利用状況 令和7年3月末まで](https://www.town.shiga-hino.lg.jp/cmsfiles/contents/0000006/6854/riyoujyoukyouR7.3.pdf)
- [利用状況 令和8年3月末まで](https://www.town.shiga-hino.lg.jp/cmsfiles/contents/0000006/6854/riyoujyoukyouR8.3.pdf)

## 🛠️ ローカルでの確認

CSV を `fetch` で読み込むため、ファイルを直接開くのではなく簡易サーバ経由で開いてください。

```bash
python3 -m http.server 8000
# → http://localhost:8000/ をブラウザで開く
```

## 🌐 GitHub Pages での公開

1. このリポジトリを自分のアカウントに作成・プッシュ
2. Settings → Pages → Build and deployment → Source を **GitHub Actions**（または **Deploy from a branch / main / root**）に設定
3. 数分後に `https://kken78.github.io/choisoko-hino-dashboard/` で公開されます

`.github/workflows/deploy.yml` を同梱しているため、main ブランチへの push で自動デプロイされます。

## 🖼️ OGP（SNS共有時のサムネ）の設定

SNSやチャットでURLを貼ったときに表示されるカード画像（`assets/ogp.png`, 1200×630px）を同梱しています。`index.html` の `<head>` 内にある OGP メタタグの **`USERNAME` と `REPO` を、自分の公開URLに2か所（`og:url` と `og:image` ／ `twitter:image`）書き換えてください。**

```html
<meta property="og:url"   content="https://kken78.github.io/choisoko-hino-dashboard/">
<meta property="og:image" content="https://kken78.github.io/choisoko-hino-dashboard/assets/ogp.png">
```

公開後、[Facebook Sharing Debugger](https://developers.facebook.com/tools/debug/) や [X Card Validator](https://cards-dev.twitter.com/validator) でキャッシュを更新すると確実に反映されます。画像を差し替えたい場合は `assets/ogp.svg` を編集して PNG に書き出してください。

## ⚠️ 免責事項

- 本リポジトリの CSV は公開 PDF から独自に抽出したものです。読み取り誤差や変換ミスを含む可能性があるため、正確な数値が必要な場合は必ず日野町の公式資料をご確認ください。
- 一部の月別利用人数・年代別構成は、原資料でのラベル・数値の重なりにより読み取りに幅があります。
- 本プロジェクトは日野町の公式システムではなく、オープンデータ推進のための実証実験（プロトタイプ）です。予告なく仕様変更・公開停止する場合があります。

## 📄 ライセンス

- **ソースコード:** [MIT License](./LICENSE)
- **公開データ (CSV):** 地域課題の解決や分析等の目的でどなたでも自由にご利用いただけます（CC BY 4.0相当を想定）。

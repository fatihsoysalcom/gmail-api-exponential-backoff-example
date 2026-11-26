# Gmail API Exponential Backoff Example

This example demonstrates how to implement exponential backoff with jitter when making API calls. This robust retry strategy is crucial for handling transient errors and rate limits, which is particularly relevant given Google's new 'timer' policies for Gmail REST APIs. By gracefully retrying failed requests, applications can adapt to varying API availability and quotas.

## Language

`python`

## How to Run

Save the code as `gmail_api_backoff.py`.
Run from your terminal: `python gmail_api_backoff.py`

## Original Article

This example accompanies the Turkish article: [Gmail REST API'lerinde Google'ın Yeni Zamanlayıcısı: Geliştiriciler Neler Yapmalı?](https://fatihsoysal.com/blog/gmail-rest-apilerinde-googlein-yeni-zamanlayicisi-gelistiriciler-neler-yapmali/).

## License

MIT — see [LICENSE](LICENSE).

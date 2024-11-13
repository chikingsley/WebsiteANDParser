# KitchenAds Monorepo

## Project Overview

This monorepo contains two main projects:
1. **KitchenAds Website**: A modern web application built with React, TypeScript, and Vite
2. **SimpleComplexParser**: A Telegram bot for deal parsing and Notion integration

## Project Structure

```
kitchenadsFINAL/
├── KitchenAdsWebsite/     # React web application
│   ├── src/               # Main source code
│   ├── public/            # Static assets
│   ├── server.js          # Express server for production
│   └── vite.config.ts     # Vite configuration
│
├── SimpleComplexParser/   # Telegram bot
│   ├── api/               # Vercel serverless functions
│   ├── bot/               # Bot logic and handlers
│   ├── main.py            # Main bot application
│   └── vercel.json        # Vercel deployment configuration
│
├── vercel.json            # Root Vercel configuration
└── .gitignore             # Gitignore for both projects
```

## Prerequisites

- Node.js 18+ (for website)
- Python 3.9+ (for Telegram bot)
- Vercel CLI
- npm or yarn

## Local Development

### KitchenAds Website

1. Navigate to the website directory
```bash
cd KitchenAdsWebsite
```

2. Install dependencies
```bash
npm install
```

3. Run development server
```bash
npm run dev
```

4. Build for production
```bash
npm run build
```

### Telegram Bot

1. Navigate to the bot directory
```bash
cd SimpleComplexParser
```

2. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Set up environment variables
Create a `.env` file with the following:
```
TELEGRAM_BOT_TOKEN=your_telegram_bot_token
NOTION_TOKEN=your_notion_token
OFFERS_DATABASE_ID=your_offers_database_id
ADVERTISERS_DATABASE_ID=your_advertisers_database_id
WEBHOOK_SECRET=your_webhook_secret
```

## Deployment to Vercel

### Automated Deployment

This repository is configured for automatic deployment to Vercel:
- Website will be deployed to the main domain
- Telegram bot will be deployed to a subdomain (bot.kitchenads.io)

### Manual Deployment

1. Install Vercel CLI
```bash
npm install -g vercel
```

2. Login to Vercel
```bash
vercel login
```

3. Deploy
```bash
vercel
```

### Environment Variables

Set the following environment variables in Vercel:
- `TELEGRAM_BOT_TOKEN`
- `NOTION_TOKEN`
- `OFFERS_DATABASE_ID`
- `ADVERTISERS_DATABASE_ID`
- `WEBHOOK_SECRET`

## Continuous Integration

- GitHub Actions configured for:
  - Linting
  - Testing
  - Deployment checks

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## Troubleshooting

### Website Issues
- Ensure Node.js and npm are up to date
- Check Vite configuration
- Verify environment variables

### Telegram Bot Issues
- Check Python and dependency versions
- Verify Telegram bot token
- Check Notion integration permissions

## License

MIT License

## Contact

For support, please open an issue in the GitHub repository or contact the maintainers.

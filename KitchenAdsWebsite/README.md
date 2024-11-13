# KitchenAds Website

A modern web application for kitchen advertising management built with React, TypeScript, and Vite.

## Features

- 📱 Responsive design for all devices
- 🎨 Modern UI with Tailwind CSS
- 🔒 Secure form handling
- 🔄 Real-time Telegram notifications
- 📊 Events management
- 🎯 Career opportunities section
- ⚡ Lightning-fast performance with Vite

## Tech Stack

- React 18
- TypeScript
- Vite
- Tailwind CSS
- Telegram Bot API
- Node.js

## Prerequisites

- Node.js 16.x or higher
- npm 7.x or higher

## Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/kitchenads.git
cd kitchenads
```

2. Install dependencies:
```bash
npm install
```

3. Create a `.env` file in the root directory and add your environment variables:
```env
TELEGRAM_BOT_TOKEN=your_telegram_bot_token
TELEGRAM_CHAT_ID=your_telegram_chat_id
VITE_APP_URL=http://localhost:5173
NODE_ENV=development
```

4. Start the development server:
```bash
npm run dev
```

The application will be available at `http://localhost:5173`

## Available Scripts

- `npm run dev` - Start development server
- `npm run build` - Build for production
- `npm run preview` - Preview production build
- `npm run lint` - Run ESLint
- `npm run type-check` - Run TypeScript type checking

## Project Structure

```
kitchenads/
├── src/
│   ├── components/     # React components
│   ├── pages/         # Page components
│   ├── api/           # API integrations
│   ├── lib/           # Utility functions
│   └── main.tsx       # Application entry point
├── public/            # Static assets
└── ...config files
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

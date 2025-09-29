# Sign.mt Integration Guide

## Overview
This guide explains how to integrate [sign.mt](https://sign.mt/) sign language translation features into your web application. Sign.mt is an AI-driven platform that provides real-time translation between spoken and signed languages.

## Features Implemented

### 1. Text-to-Sign Language (`text-to-sign.html`)
- Converts written text into sign language videos
- Supports multiple sign languages (ASL, ISL, BSL)
- Auto-detection of input language
- Multiple avatar styles (realistic, cartoon, minimal)
- Download functionality for generated videos

### 2. Sign Language-to-Text (`sign-to-text.html`)
- Converts sign language gestures into written text
- Real-time camera-based recognition
- Support for multiple sign languages
- Confidence level indicators
- Auto-detection of sign language type

## API Integration Steps

### Step 1: Get API Access
1. Visit [sign.mt](https://sign.mt/)
2. Contact the team for API access and documentation
3. Obtain your API key and endpoint URLs

### Step 2: Update API Calls

#### Text-to-Sign Language API
Replace the placeholder `callSignMTAPI` function in `text-to-sign.html`:

```javascript
async callSignMTAPI(text, language) {
    const response = await fetch('https://api.sign.mt/text-to-sign', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${YOUR_API_KEY}`
        },
        body: JSON.stringify({
            text: text,
            target_language: language,
            avatar_style: this.avatarSelect.value,
            quality: 'high'
        })
    });
    
    if (!response.ok) {
        throw new Error(`API Error: ${response.status}`);
    }
    
    const data = await response.json();
    return data.video_url;
}
```

#### Sign Language-to-Text API
Replace the placeholder `callSignRecognitionAPI` function in `sign-to-text.html`:

```javascript
async callSignRecognitionAPI(imageData) {
    const response = await fetch('https://api.sign.mt/sign-to-text', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${YOUR_API_KEY}`
        },
        body: JSON.stringify({
            image_data: imageData,
            sign_language: this.currentLang,
            confidence_threshold: parseFloat(this.confidenceSelect.value)
        })
    });
    
    if (!response.ok) {
        throw new Error(`API Error: ${response.status}`);
    }
    
    const data = await response.json();
    return {
        text: data.translated_text,
        confidence: data.confidence
    };
}
```

### Step 3: Environment Variables
Create a `.env` file in your project root:

```env
SIGN_MT_API_KEY=your_api_key_here
SIGN_MT_BASE_URL=https://api.sign.mt
```

### Step 4: Update Configuration
Add API configuration to your JavaScript files:

```javascript
const SIGN_MT_CONFIG = {
    apiKey: process.env.SIGN_MT_API_KEY || 'your_api_key_here',
    baseUrl: process.env.SIGN_MT_BASE_URL || 'https://api.sign.mt',
    timeout: 30000 // 30 seconds
};
```

## Supported Languages

### Spoken Languages
- English (en)
- Hindi (hi)
- Spanish (es)
- French (fr)
- German (de)
- And 35+ more languages

### Sign Languages
- American Sign Language (ASL)
- Indian Sign Language (ISL)
- British Sign Language (BSL)
- International Sign (IS)
- And 40+ more sign languages

## Avatar Customization

### Available Styles
- **Realistic**: Photo-realistic avatars
- **Cartoon**: Stylized cartoon avatars
- **Minimal**: Simple, clean avatars

### Customization Options
```javascript
const avatarOptions = {
    style: 'realistic', // realistic, cartoon, minimal
    gender: 'neutral', // male, female, neutral
    age: 'adult', // child, teen, adult, senior
    skin_tone: 'medium', // light, medium, dark
    clothing: 'casual' // casual, formal, professional
};
```

## Error Handling

### Common Error Codes
- `400`: Bad Request - Invalid input parameters
- `401`: Unauthorized - Invalid API key
- `403`: Forbidden - Insufficient permissions
- `429`: Too Many Requests - Rate limit exceeded
- `500`: Internal Server Error - Server-side error

### Error Handling Implementation
```javascript
async handleAPIError(error) {
    if (error.status === 401) {
        this.showStatus('Invalid API key. Please check your configuration.', 'error');
    } else if (error.status === 429) {
        this.showStatus('Rate limit exceeded. Please try again later.', 'error');
    } else if (error.status >= 500) {
        this.showStatus('Server error. Please try again later.', 'error');
    } else {
        this.showStatus(`Error: ${error.message}`, 'error');
    }
}
```

## Performance Optimization

### 1. Video Compression
```javascript
// Compress video before sending to API
const compressedImageData = await this.compressImage(imageData, 0.8);
```

### 2. Caching
```javascript
// Cache generated videos
const videoCache = new Map();
if (videoCache.has(text)) {
    return videoCache.get(text);
}
```

### 3. Debouncing
```javascript
// Debounce recognition calls
const debouncedRecognize = debounce(this.recognizeSigns.bind(this), 1000);
```

## Testing

### Test Cases
1. **Text-to-Sign**: Test with various languages and text lengths
2. **Sign-to-Text**: Test with different sign languages and lighting conditions
3. **Error Handling**: Test with invalid inputs and network errors
4. **Performance**: Test with large texts and long recognition sessions

### Test Data
```javascript
const testCases = {
    textToSign: [
        { text: "Hello, how are you?", language: "english" },
        { text: "नमस्ते, आप कैसे हैं?", language: "hindi" },
        { text: "Bonjour, comment allez-vous?", language: "french" }
    ],
    signToText: [
        { language: "asl", expected: "hello" },
        { language: "isl", expected: "नमस्ते" },
        { language: "bsl", expected: "hello" }
    ]
};
```

## Security Considerations

### 1. API Key Protection
- Never expose API keys in client-side code
- Use environment variables
- Implement server-side proxy if needed

### 2. Data Privacy
- Ensure user data is handled securely
- Implement proper data retention policies
- Comply with privacy regulations (GDPR, CCPA)

### 3. Input Validation
```javascript
function validateTextInput(text) {
    if (!text || text.length > 1000) {
        throw new Error('Invalid text input');
    }
    return text.trim();
}
```

## Deployment

### 1. Environment Setup
```bash
# Install dependencies
npm install

# Set environment variables
export SIGN_MT_API_KEY=your_api_key_here

# Start the application
npm start
```

### 2. Production Configuration
```javascript
const config = {
    apiKey: process.env.SIGN_MT_API_KEY,
    baseUrl: process.env.NODE_ENV === 'production' 
        ? 'https://api.sign.mt' 
        : 'https://staging-api.sign.mt',
    timeout: 30000
};
```

## Support and Resources

### Documentation
- [Sign.mt Official Website](https://sign.mt/)
- [API Documentation](https://sign.mt/docs) (contact for access)
- [GitHub Repository](https://github.com/sign-mt) (if available)

### Contact
- Email: support@sign.mt
- Website: https://sign.mt/contact

### Community
- Join the Sign.mt community for updates and support
- Contribute to the open-source project
- Share your integration experiences

## Changelog

### Version 1.0.0
- Initial implementation of Text-to-Sign Language
- Initial implementation of Sign Language-to-Text
- Basic UI components and navigation
- Placeholder API integration ready for real API

### Future Enhancements
- Real-time video streaming
- Batch processing capabilities
- Advanced avatar customization
- Offline functionality
- Mobile app integration

## License
This integration follows the Sign.mt terms of service and API usage guidelines. Please review the official terms before deploying to production.
# ResuMate: Resume Review Application

An AI-powered web application that provides professional feedback on resumes using Google Gemini API. Upload your resume in PDF or DOCX format and receive detailed suggestions for improvement through an intuitive interface.

## 🚀 Key Features

- **Smart Resume Analysis**: Leverages Google Gemini API to provide professional, context-aware feedback
- **Multiple Format Support**: Handles both PDF and DOCX resume formats
- **Secure File Processing**: Implements robust file validation and secure handling
- **User-Friendly Interface**: Clean, intuitive web interface for easy resume uploads
- **Comprehensive Feedback**: Provides actionable suggestions and an improved version of your resume

## 🛠️ Technology Stack

- **Backend**: Python 3.9+ with FastHTML framework
- **AI Service**: Google Gemini API
- **Package Management**: uv (from Astral)
- **File Processing**: PyPDF2, python-docx
- **Configuration**: python-dotenv

## 📁 Project Structure

```
resume-review-app/
├── main.py                # Application entry point and routes
├── gemini.py             # Gemini API integration
├── file_processing.py    # File handling utilities
├── static/               # Static assets
├── .env                  # Environment configuration
├── requirements.txt      # Dependencies
└── README.md            # Documentation
```

## 🚦 Prerequisites

1. Python 3.9 or higher
2. Google Gemini API key
3. uv package manager:
   ```bash
   pip install uv
   ```

## ⚡ Quick Start

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/resume-review-app.git
   cd resume-review-app
   ```

2. **Set up environment variables**
   ```bash
   # Create and edit .env file
   echo "GEMINI_API_KEY=your_api_key_here" > .env
   ```

3. **Install dependencies**
   ```bash
   uv pip install -r requirements.txt
   ```

4. **Start the server**
   ```bash
   python main.py
   ```

5. **Access the application**
   ```
   http://localhost:8000
   ```

## ⚙️ Configuration Options

### Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `GEMINI_API_KEY` | Google Gemini API key | Required |
| `MAX_FILE_SIZE` | Maximum upload file size | 5MB |
| `ALLOWED_TYPES` | Allowed file formats | PDF, DOCX |

### File Upload Specifications

- **Maximum File Size**: 5MB
- **Supported Formats**: 
  - PDF (`application/pdf`)
  - DOCX (`application/vnd.openxmlformats-officedocument.wordprocessingml.document`)

## 🔍 Troubleshooting Guide

### Missing Favicon
```bash
# Ensure favicon exists
cp your-favicon.ico static/favicon.ico
```

### Upload Errors
1. Verify file size is under 5MB
2. Confirm file format is PDF or DOCX
3. Check permissions on upload directory

### API Issues
1. Verify API key in `.env`
2. Check Google Cloud Console permissions
3. Monitor API usage limits

## 📦 Dependencies

```plaintext
fasthtml==0.9.2
python-dotenv==1.0.0
PyPDF2==3.0.1
python-docx==0.8.11
google-generativeai==0.3.2
uv==0.1.0
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [FastHTML](https://fasthtml.io) - Web framework
- [Google Gemini API](https://cloud.google.com/gemini) - AI capabilities
- [uv](https://github.com/astral/uv) - Package management

## 📮 Support

For support, please:
1. Check the [Troubleshooting Guide](#-troubleshooting-guide)
2. Open an issue for bugs or feature requests
3. Join our [Discord community](https://discord.gg/resume-review-app)

---
**Note**: Replace placeholder URLs and values with your actual project information before deploying.
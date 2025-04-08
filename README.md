# BudgetronAI

![Version](https://img.shields.io/badge/version-1.0.0--alpha-blue)
![License](https://img.shields.io/badge/license-MIT-green)

**Intelligent family financial management powered by AI**

## 📋 Description

BudgetronAI is a comprehensive web application for family finance management that integrates artificial intelligence to provide personalized advice and in-depth analysis. Designed for families who want to optimize their financial situation in a simple and intuitive way.

## 🚀 MVP Definition

Our Minimum Viable Product (MVP) will include:

1. **Core User Management**
   - Account creation and authentication
   - Basic profile management
   - Family profile setup

2. **Financial Tracking**
   - Manual expense entry with categorization
   - Transaction history and basic filtering
   - Basic dashboard with spending overview

3. **Budgeting Essentials**
   - Monthly budget creation based on 50/30/20 rule
   - Budget vs. actual comparison
   - Expense category breakdown

4. **Basic AI Features**
   - Automatic transaction categorization
   - Simple financial advisor Q&A
   - Basic spending pattern identification

## ✨ Features (Full Version)

### Financial Management
- 📊 Expense tracking with automatic categorization
- 💰 Smart budgeting based on the 50/30/20 rule
- 🎯 Monitoring of personalized savings goals
- 🛡️ Emergency fund with automatic calculation of the ideal amount
- 📈 Low-risk investment analysis

### Artificial Intelligence
- 🤖 Virtual financial advisor that answers your questions
- 🔮 Predictive analysis of spending trends
- 💡 Personalized advice based on your financial profile
- 🎓 Contextual financial education
- 💸 Identification of savings opportunities

## 👥 Team Structure

Our development team consists of:

- **Tech Lead/Architect**: Oversees technical direction, architecture decisions, and project coordination
- **.NET Specialist**: Focuses on backend development, database design, and API implementation
- **AI/Python Specialist**: Develops AI services, machine learning models, and data analysis components
- **UI/UX Developer**: (Part-time/shared role) Handles Blazor frontend and user experience

Each team member is expected to:
- Participate in cross-functional activities when needed
- Follow the established development workflow
- Contribute to documentation and testing
- Participate in daily stand-ups and weekly technical discussions

## 👥 Contributors

- [Casimiro](https://github.com/dracmos)

## 🏗️ Architecture

BudgetronAI uses a hybrid architecture that leverages .NET for the core application and Python for artificial intelligence services, organized in containerized microservices.

### Architectural Scheme

```
Browser/Mobile App --> API Gateway --> .NET Backend / AI Services
```

### Main Components

#### Frontend
- **Blazor WebAssembly** for the SPA web interface
- **PWA** for lightweight mobile access

#### Backend (.NET)
- **ASP.NET Core API** organized according to Domain-Driven Design (DDD) principles
- **Entity Framework Core** for database access
- **Identity Server / OpenIddict** for authentication and authorization
- **SignalR** for real-time updates

#### API Gateway
- **YARP** (Yet Another Reverse Proxy) for routing, centralized authentication, and rate limiting

#### AI Services (Python)
- **FastAPI** to expose AI services as REST APIs
- **Scikit-learn/Pandas** for data analysis and machine learning
- **Transformers/spaCy** for natural language processing
- **MLflow** for model versioning and tracking

#### Infrastructure
- **PostgreSQL** for the main database
- **Redis** for caching
- **RabbitMQ** for event-driven communication between services
- **OpenTelemetry** with Elasticsearch/Kibana for centralized logging
- **Prometheus/Grafana** for monitoring and metrics
- **HashiCorp Vault** for secrets management

## 🛠️ Technology Stack

### Backend
- .NET 8
- Entity Framework Core
- ASP.NET Core Identity
- SignalR
- YARP

### Frontend
- Blazor WebAssembly
- Tailwind CSS
- Chart.js
- SignalR Client

### AI Services
- Python 3.11+
- FastAPI
- scikit-learn
- Pandas
- spaCy/Transformers
- MLflow

### Database and Storage
- PostgreSQL
- Redis

### DevOps
- Docker
- GitHub Actions (CI/CD)

## 📋 Prerequisites

- .NET 8 SDK
- Docker Desktop
- Python 3.11+
- PostgreSQL 14+
- Visual Studio 2022 or JetBrains Rider

## 🚀 Installation and Setup

### Development Environment Setup

```bash
# Clone the repository
git clone https://github.com/yourorg/BudgetronAI.git
cd BudgetronAI

# Configure the .NET backend
cd src/Backend
dotnet restore
dotnet build

# Configure the Blazor frontend
cd ../Frontend
dotnet restore
dotnet build

# Configure the AI services
cd ../AIServices
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt

# Start Docker services
cd ../../
docker-compose up -d

# Start the application in development mode
dotnet run --project src/Backend/BudgetronAI.API
```

### Using Docker Compose (All services)

```bash
docker-compose up -d
```

### Troubleshooting

- **Docker Compose Issues**: Ensure Docker Desktop is running and ports aren't in use
- **Database Connection**: Check PostgreSQL service is running in Docker
- **Python Environment**: Verify Python version compatibility (3.11+)
- **Frontend Build Failures**: Check Node.js version (16+) if using npm packages

## 📂 Project Structure

```
BudgetronAI/
├── src/
│   ├── Backend/
│   │   ├── BudgetronAI.API/
│   │   ├── BudgetronAI.Application/
│   │   ├── BudgetronAI.Domain/
│   │   ├── BudgetronAI.Infrastructure/
│   │   └── BudgetronAI.Tests/
│   ├── Frontend/
│   │   ├── BudgetronAI.Blazor/
│   │   └── BudgetronAI.Shared/
│   ├── AIServices/
│   │   ├── CategoryPrediction/
│   │   ├── FinancialAdvisor/
│   │   ├── SpendingAnalysis/
│   │   └── ModelTraining/
│   └── Gateway/
│       └── BudgetronAI.Gateway/
├── infrastructure/
│   └── docker-compose.yml
├── docs/
│   ├── architecture/
│   ├── api/
│   └── user-guides/
├── scripts/
├── README.md
└── LICENSE
```

## 🔄 Development Workflow

### Git Workflow

1. Work on feature branches named `feature/feature-name`
2. Create PRs to `develop` branch
3. Releases are merged from `develop` to `main`

### Pull Request Process

1. Ensure code passes all automated tests
2. Requires at least one code review approval
3. Must pass CI/CD pipeline checks
4. Update documentation if needed

### Code Review Standards

- Focus on architecture, security, and performance 
- Use constructive feedback
- Review within 24 hours when possible
- Automated style checks handle formatting issues

## 👨‍💻 Contribution Guidelines

To contribute to BudgetronAI:

1. Fork the repository
2. Create a branch for your feature (`git checkout -b feature/amazing-feature`)
3. Follow the coding standards in the Development Standards Guide (see docs/development-standards.md)
4. Write unit tests for new functionality
5. Update documentation as needed
6. Commit your changes (`git commit -m 'Add some amazing feature'`)
7. Push to the branch (`git push origin feature/amazing-feature`)
8. Open a Pull Request against the `develop` branch

## 🔄 Development Strategy

The project follows a phased development approach as outlined in our Roadmap document (see docs/roadmap.md).

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
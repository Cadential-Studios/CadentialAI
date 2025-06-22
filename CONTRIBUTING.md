# Contributing to CadentialAI

Thank you for your interest in contributing to CadentialAI! This project is a personal Windows AI assistant built on Microsoft's UFO² framework.

## 🚀 Getting Started

### Prerequisites
- Windows 10 or later
- Python 3.10 or 3.11
- Git

### Setting up the Development Environment

1. **Fork and Clone the Repository**
   ```powershell
   git clone https://github.com/Cadential-Studios/CadentialAI.git
   cd CadentialAI
   ```

2. **Create a Virtual Environment**
   ```powershell
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   ```

3. **Install Dependencies**
   ```powershell
   pip install -r requirements.txt
   ```

4. **Set up Configuration**
   - Copy configuration templates from `UFO/config/`
   - Add your API keys and personal settings

## 🤝 How to Contribute

### Types of Contributions Welcome

- **Bug Reports**: Found a bug? Please report it!
- **Feature Requests**: Have an idea for improving the assistant?
- **Code Contributions**: Bug fixes, new features, optimizations
- **Documentation**: Improve docs, examples, or tutorials
- **Testing**: Write tests or improve existing test coverage

### Submitting Changes

1. **Create a Feature Branch**
   ```powershell
   git checkout -b feature/your-feature-name
   ```

2. **Make Your Changes**
   - Follow the existing code style
   - Add tests for new functionality
   - Update documentation as needed

3. **Test Your Changes**
   ```powershell
   pytest tests/
   ```

4. **Commit Your Changes**
   ```powershell
   git commit -m "feat: add your feature description"
   ```

5. **Push and Create Pull Request**
   ```powershell
   git push origin feature/your-feature-name
   ```

### Commit Message Convention

We use conventional commits:
- `feat:` for new features
- `fix:` for bug fixes
- `docs:` for documentation changes
- `test:` for adding or modifying tests
- `refactor:` for code refactoring

## 📋 Guidelines

### Code Style
- Follow PEP 8 for Python code
- Use meaningful variable and function names
- Add docstrings for functions and classes
- Keep functions focused and small

### Testing
- Write unit tests for new functionality
- Ensure all tests pass before submitting
- Aim for good test coverage

### Documentation
- Update README.md if adding new features
- Add inline comments for complex logic
- Update configuration examples when needed

## 🐛 Reporting Issues

When reporting issues, please include:
- Windows version
- Python version
- Steps to reproduce
- Expected vs actual behavior
- Error messages or logs
- Screenshots if relevant

## 💡 Feature Requests

For feature requests:
- Explain the use case
- Describe the proposed solution
- Consider alternative approaches
- Discuss potential impact

## 📞 Getting Help

- **Documentation**: Check the [project docs](./docs/)
- **Issues**: Search existing issues first
- **Discussions**: Use GitHub Discussions for questions

## 🙏 Recognition

Contributors will be recognized in:
- README.md contributors section
- Release notes
- Project documentation

## 📜 License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

Thank you for helping make CadentialAI better! 🎉

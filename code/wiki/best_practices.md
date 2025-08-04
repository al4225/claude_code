# Claude Code Best Practices and Query Format Guide

## Query Format Recommendations

### 1. Be Specific and Clear

#### ❌ Poor Examples:
```
"fix code"
"make it better"
"debug"
"help"
```

#### ✅ Good Examples:
```
"Fix the TypeError in line 42 of user_auth.py"
"Optimize the database query in get_user_data() function for better performance"
"Debug the login function that's returning 'undefined' instead of user object"
"Help me implement rate limiting for the API endpoints"
```

### 2. Provide Context

#### ❌ Poor Example:
```
"Add authentication"
```

#### ✅ Good Example:
```
"Add JWT authentication to my Express.js REST API. I already have a User model with MongoDB. Need login and register endpoints."
```

### 3. Use Structured Requests

#### Template for Complex Tasks:
```
Goal: [What you want to achieve]
Current State: [What exists now]
Requirements: [Specific requirements]
Constraints: [Any limitations]
Preferred Approach: [If you have preferences]
```

#### Example:
```
Goal: Create a file upload system
Current State: Basic Express server with user authentication
Requirements: 
- Support images and PDFs up to 10MB
- Store metadata in PostgreSQL
- Files in AWS S3
Constraints: Must use existing authentication middleware
Preferred Approach: Use multer for handling uploads
```

## Planning Workflow

### 1. Task Decomposition

#### For Complex Features:
```
Step 1: "Help me plan the implementation of a real-time chat feature"
Step 2: "Let's implement the WebSocket server setup"
Step 3: "Now add the message broadcasting logic"
Step 4: "Create the client-side connection handler"
Step 5: "Add message persistence to the database"
```

### 2. Iterative Development

Start simple, then enhance:
```
Iteration 1: "Create a basic calculator with add and subtract"
Iteration 2: "Add multiply and divide operations"
Iteration 3: "Add memory functions (M+, M-, MR, MC)"
Iteration 4: "Add keyboard support and improve UI"
```

## Code Quality Practices

### 1. Regular Code Reviews
```
After implementation:
"Review the authentication system I just created for security vulnerabilities"
"Check the performance of the data processing functions"
"Suggest improvements for code maintainability"
```

### 2. Testing Strategy
```
"Write unit tests for the UserService class"
"Create integration tests for the API endpoints"
"Add edge case tests for the input validation"
```

### 3. Documentation
```
"Generate API documentation for the REST endpoints"
"Add JSDoc comments to all public functions"
"Create a README with setup instructions"
```

## Effective Communication Patterns

### 1. Progressive Disclosure
```
Initial: "I need a user management system"
Follow-up: "It should support roles: admin, editor, viewer"
Details: "Admins can create/delete users, editors can modify content, viewers read-only"
```

### 2. Error Reporting
```
Bad: "It doesn't work"
Good: "Getting 'TypeError: Cannot read property 'id' of undefined' when calling getUserProfile() with a valid token"
```

### 3. Feature Requests
```
Template:
"I want to add [feature]
It should [behavior]
When [condition]
So that [benefit]"

Example:
"I want to add email notifications
It should send an email to users
When their order status changes
So that they stay informed about their purchase"
```

## Common Patterns and Solutions

### 1. CRUD Operations
```
"Create a complete CRUD API for [Model] with:
- Input validation
- Error handling
- Pagination for list endpoint
- Filtering and sorting options"
```

### 2. Authentication Flow
```
"Implement secure authentication with:
- Password hashing using bcrypt
- JWT tokens with refresh tokens
- Password reset via email
- Account activation"
```

### 3. File Processing
```
"Create a file processing system that:
- Validates file types and sizes
- Generates thumbnails for images
- Extracts metadata
- Handles errors gracefully"
```

## Debugging Strategies

### 1. Systematic Approach
```
"My app crashes when uploading files. Here's what I've tried:
1. Checked file size limits - OK
2. Verified permissions - OK
3. Console shows 'ENOENT' error
Please help debug starting from the file handling middleware"
```

### 2. Providing Error Context
```
"Error: Connection refused
Environment: Node.js 18, PostgreSQL 14
Code: [paste relevant code]
Config: [paste config]
What I've checked: Database is running, credentials are correct"
```

## Performance Optimization

### 1. Specific Metrics
```
"The /api/search endpoint takes 3+ seconds. Help me optimize:
- Current: Searches through 100k records
- Database: PostgreSQL with no indexes
- Goal: Response time under 500ms"
```

### 2. Profiling Request
```
"Profile the image processing function and suggest optimizations.
Current behavior: Processes 10 images/second
Target: 50 images/second
Constraints: Limited to 2GB RAM"
```

## Project Organization

### 1. Architecture Decisions
```
"I'm building a microservices architecture. Help me decide:
- Service boundaries for user, product, and order domains
- Communication: REST vs message queue
- Data consistency strategy"
```

### 2. Technology Stack
```
"Help me choose between:
Option A: Next.js + Prisma + PostgreSQL
Option B: Express + TypeORM + MySQL
Use case: E-commerce platform with 10k daily users
Priorities: Developer experience, performance, scalability"
```

## Learning and Exploration

### 1. Concept Explanation
```
"Explain how JWT refresh tokens work and implement a secure rotation strategy"
"Show me the difference between SQL and NoSQL with practical examples"
```

### 2. Best Practice Inquiry
```
"What's the current best practice for:
- Storing secrets in Node.js applications
- Handling database migrations
- Structuring a large React application"
```

## Collaboration Commands

### 1. Code Handoff
```
"Document this function so another developer can understand:
- What it does
- Expected inputs/outputs  
- Error cases
- Usage examples"
```

### 2. Team Integration
```
"Set up pre-commit hooks for:
- Code formatting (Prettier)
- Linting (ESLint)
- Unit test execution
- Commit message validation"
```

## Remember

1. **Start with Why**: Explain what you're trying to achieve, not just what's broken
2. **Be Iterative**: Complex problems are best solved step by step
3. **Provide Examples**: When asking for something specific, show what you expect
4. **Ask for Explanations**: Don't hesitate to ask why a solution works
5. **Version Everything**: Always mention versions of languages, frameworks, and tools

## Quick Templates

### Bug Report:
```
What happened: [Describe the issue]
Expected behavior: [What should happen]
Steps to reproduce: [How to trigger]
Environment: [OS, versions, etc.]
Error messages: [Exact error text]
```

### Feature Request:
```
Feature: [Name]
User Story: As a [role], I want [feature] so that [benefit]
Acceptance Criteria: [List of requirements]
Technical Constraints: [Any limitations]
```

### Code Review Request:
```
File/Function: [What to review]
Concerns: [Specific areas of concern]
Context: [Why this code exists]
Performance Requirements: [If applicable]
```
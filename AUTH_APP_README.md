# Simple Authentication App

A full-stack authentication application with user registration and login functionality built with Angular (TypeScript/JavaScript) frontend and Java Spring Boot backend.

## Project Structure

```
project/
├── backend/                    # Java Spring Boot Backend
│   ├── src/main/java/com/example/auth/
│   │   ├── AuthApplication.java           # Main application class
│   │   ├── controller/
│   │   │   └── AuthController.java        # REST API endpoints
│   │   ├── service/
│   │   │   ├── UserDetailsImpl.java       # UserDetails implementation
│   │   │   └── UserDetailsServiceImpl.java # User service
│   │   ├── model/
│   │   │   ├── User.java                  # User entity
│   │   │   ├── LoginRequest.java          # Login DTO
│   │   │   ├── SignupRequest.java         # Registration DTO
│   │   │   └── JwtResponse.java           # JWT response DTO
│   │   ├── repository/
│   │   │   └── UserRepository.java        # User repository
│   │   └── config/
│   │       ├── WebSecurityConfig.java     # Security configuration
│   │       ├── JwtUtils.java              # JWT utilities
│   │       ├── AuthEntryPointJwt.java     # JWT entry point
│   │       └── AuthTokenFilter.java       # JWT filter
│   ├── src/main/resources/
│   │   └── application.properties         # Application configuration
│   └── pom.xml                           # Maven configuration
└── frontend/                   # Angular Frontend
    ├── src/app/
    │   ├── components/
    │   │   ├── login/                     # Login component
    │   │   ├── register/                  # Registration component
    │   │   └── dashboard/                 # Dashboard component
    │   ├── services/
    │   │   └── auth.service.ts            # Authentication service
    │   ├── models/
    │   │   └── user.model.ts              # TypeScript models
    │   ├── guards/
    │   │   └── auth.guard.ts              # Route guard
    │   ├── app.component.*                # Root component
    │   ├── app.module.ts                  # App module
    │   └── app-routing.module.ts          # Routing configuration
    ├── src/styles.css                     # Global styles
    ├── src/index.html                     # Main HTML file
    ├── package.json                       # NPM configuration
    └── angular.json                       # Angular configuration
```

## Features

### Backend (Java Spring Boot)
- **User Registration**: Create new user accounts with validation
- **User Authentication**: Login with username/password
- **JWT Token**: Secure authentication using JSON Web Tokens
- **Password Encryption**: BCrypt password hashing
- **H2 Database**: In-memory database for development
- **Spring Security**: Comprehensive security configuration
- **CORS Support**: Cross-origin resource sharing enabled
- **RESTful API**: Clean REST endpoints for auth operations

### Frontend (Angular)
- **User Registration Form**: Responsive form with validation
- **User Login Form**: Clean login interface
- **Dashboard**: Protected user dashboard
- **Route Guards**: Protect routes that require authentication
- **JWT Storage**: Local storage management for tokens
- **Bootstrap UI**: Responsive design with Bootstrap 5
- **Form Validation**: Client-side and server-side validation
- **Error Handling**: User-friendly error messages

## API Endpoints

### Authentication
- `POST /api/auth/signup` - Register a new user
- `POST /api/auth/signin` - Login user
- `GET /api/auth/test` - Test endpoint

### Database Console (Development)
- `GET /h2-console` - H2 Database console (username: sa, password: empty)

## Prerequisites

### Backend
- Java 17 or higher
- Maven 3.6+

### Frontend
- Node.js 16+ 
- npm or yarn
- Angular CLI

## Installation & Setup

### Backend Setup
1. Navigate to the backend directory:
   ```bash
   cd backend
   ```

2. Install dependencies and run:
   ```bash
   mvn clean install
   mvn spring-boot:run
   ```

3. The backend server will start on `http://localhost:8080`

### Frontend Setup
1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Install Angular CLI globally (if not already installed):
   ```bash
   npm install -g @angular/cli
   ```

4. Start the development server:
   ```bash
   ng serve
   ```

5. The frontend application will start on `http://localhost:4200`

## Usage

1. **Start Backend**: Run the Spring Boot application on port 8080
2. **Start Frontend**: Run the Angular application on port 4200
3. **Register**: Create a new account at `/register`
4. **Login**: Login with your credentials at `/login`
5. **Dashboard**: Access the protected dashboard after login

## Configuration

### Backend Configuration
Edit `backend/src/main/resources/application.properties`:
```properties
# Server port
server.port=8080

# Database configuration
spring.datasource.url=jdbc:h2:mem:testdb
spring.datasource.username=sa
spring.datasource.password=

# JWT configuration
app.jwtSecret=mySecretKey123456789012345678901234567890
app.jwtExpirationMs=86400000
```

### Frontend Configuration
The frontend is configured to connect to the backend at `http://localhost:8080`. To change this, update the `AUTH_API` constant in `auth.service.ts`.

## Security Features

- **Password Hashing**: BCrypt encryption for stored passwords
- **JWT Authentication**: Stateless authentication using JSON Web Tokens
- **CORS Configuration**: Proper cross-origin resource sharing setup
- **Input Validation**: Both client-side and server-side validation
- **Route Protection**: Angular route guards prevent unauthorized access

## Development Features

- **H2 Console**: Access database console at `/h2-console`
- **Hot Reload**: Both frontend and backend support hot reloading
- **Error Handling**: Comprehensive error handling on both ends
- **Responsive Design**: Mobile-friendly Bootstrap UI

## Technology Stack

### Backend
- **Java 17**: Programming language
- **Spring Boot 3.1**: Application framework
- **Spring Security**: Authentication and authorization
- **Spring Data JPA**: Data persistence
- **H2 Database**: In-memory database
- **JWT**: JSON Web Token for authentication
- **Maven**: Dependency management

### Frontend
- **Angular 16**: Frontend framework
- **TypeScript**: Programming language
- **Bootstrap 5**: CSS framework
- **RxJS**: Reactive programming
- **Angular Forms**: Form handling
- **Angular Router**: Navigation

## Future Enhancements

- Add user roles and permissions
- Implement password reset functionality
- Add user profile management
- Switch to PostgreSQL for production
- Add email verification
- Implement refresh tokens
- Add social media login
- Add unit and integration tests

## Troubleshooting

### Common Issues

1. **CORS Errors**: Ensure backend CORS is properly configured
2. **Port Conflicts**: Check if ports 8080 and 4200 are available
3. **JWT Expiration**: Tokens expire after 24 hours by default
4. **Database Issues**: H2 database resets on application restart

### Development Tips

- Use browser developer tools to debug API calls
- Check browser console for JavaScript errors
- Monitor backend logs for server-side issues
- Use H2 console to inspect database state

## License

This is a simple demonstration application. Feel free to use and modify as needed.

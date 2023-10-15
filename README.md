# Sensor Monitoring System

API based web application designed to streamline ticket management, making it the ideal solution for Issue Tracking Systems. This application is built with simplicity and flexibility in mind, using Flask as the core framework and MySQL as the database.

## Table of Contents
- [Components](#components)
- [Requirements](#requirements)
- [Highlights](#Highlights)
- [Usage](#usage)
- [Contribution](#contribution)

## Components
- **Framework:** Flask.
- **Database:** MySQL.

## Requirements
- Docker
- Docker Compose

## Highlights
- **Modular Structure:** The project follows the Factory Pattern, enabling a well-structured and maintainable codebase.
- **JWT Authentication:** The application incorporates a robust JWT (JSON Web Token) authentication system, providing secure access for registered users with functionality of Token refresh and Token expire.

## Usage

- **User Registration:** New users can quickly and securely register themselves, obtaining a Access Token (JWT) to access the system.
- **User Login:** Registered users can easily Log In and receive their Access Token for authentication.
- **Ticket Creation:** Users can create ticket, providing a ticket code.
- **Branch Management:** Users can efficiently create and manage multiple branches within each ticket code, each with a unique name.
- **Progress Track:** Users can change the status of both individual tickets and branches to track progress and current state of tasks and issues.

## Contribution

We look forward to your contributions in implementing the frontend of the application.

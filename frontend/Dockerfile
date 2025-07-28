# FTracker/frontend/Dockerfile

# Use official Node.js image as the base
FROM node:20-alpine

# Set working directory
WORKDIR /app

# Copy package.json and package-lock.json (if available)
COPY package.json ./
COPY package-lock.json ./

# Install dependencies
RUN npm install

# Copy the rest of the app source code
COPY . ./

# Expose the port the app runs on
EXPOSE 3000

# Start the React development server
CMD ["npm", "start"]

# FTracker/frontend/Dockerfile

# Use official Node.js image as the base
FROM node:20-alpine

# Set working directory
WORKDIR /app

# Copy package.json and package-lock.json from ftracker subfolder
COPY ftracker/package.json ./package.json
COPY ftracker/package-lock.json ./package-lock.json

# Install dependencies
RUN npm install

# Copy the rest of the app source code from ftracker subfolder
COPY ftracker/ ./

# Expose the port the app runs on
EXPOSE 3000

# Start the React development server
CMD ["npm", "start"]

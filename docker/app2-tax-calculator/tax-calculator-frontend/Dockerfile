FROM node:24-slim AS build
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .

# this command is used to build if we are using react-vite application or simply compile React/Vite app -> creates /app/dist folder
RUN npm run build
# multi-stage build: stage 1 builds the app, stage 2 serves it via nginx advantage is this keeps the final image small by discarding build tools
FROM nginx:alpine
# this line will take all the previous built from /app/dist folder and will transfer it to this location /usr/share/nginx on nginx server
COPY --from=build /app/dist /usr/share/nginx/html

EXPOSE 80

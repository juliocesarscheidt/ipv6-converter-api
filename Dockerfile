FROM node:alpine as builder
LABEL maintainer="julio@blackdevs.com.br"

# node build
WORKDIR /app
COPY package.json /app
RUN npm install
COPY . /app
RUN npm run build

# nginx server
FROM nginx
EXPOSE 80
COPY --from=builder /app/dist /usr/share/nginx/html

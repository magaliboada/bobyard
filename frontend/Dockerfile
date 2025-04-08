FROM node:16

WORKDIR /app

COPY package.json package-lock.json ./

RUN npm install

COPY . .

EXPOSE 8080

ENV VITE_HOST=0.0.0.0
ENV VITE_PORT=8080

RUN chown -R node:node /app

USER node

CMD ["npm", "run", "dev"]

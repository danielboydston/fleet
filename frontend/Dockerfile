FROM node:20

WORKDIR /usr/src/app

COPY app/package*.json ./

RUN npm install
# If you are building your code for production
# RUN npm ci --omit=dev

# Bundle app source
COPY app/ .

EXPOSE 3000
CMD [ "node", "server.js" ]
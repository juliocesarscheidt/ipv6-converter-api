const express = require('express');
const app = express();
const proxy = require('express-http-proxy');

const host = process.env.HOST || 'localhost';
const port = process.env.PORT || 5000;

const targetHost = process.env.TARGET_HOST || 'localhost';
const targetPort = process.env.TARGET_PORT || 8080;

const swaggerUi = require('swagger-ui-express');
const YAML = require('yamljs');
const swaggerDocumentValidIPv4 = YAML.load('./docs/julio-cesar-ipv6-converter-api-1.0.0-swagger.yaml');

app.use('/api/v1', proxy(`http://${targetHost}:${targetPort}/`, {
    proxyReqPathResolver: (req) => {
      const reqUrl = req.url || '';
      console.info(`Request at => ${reqUrl}`);
      return `/api/v1${reqUrl}`;
    }
  }
));

const options = {
  explorer: true,
}

app.use('/swagger-docs', swaggerUi.serve, swaggerUi.setup(swaggerDocumentValidIPv4, options));

app.listen(port, host, () => {
  console.info(`Listening at http://${host}:${port}`);
});

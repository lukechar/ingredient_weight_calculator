source /opt/python/current/env
# set domain name in the environment variable as SSL_DOMAIN
# echo $SSL_DOMAIN
# set email in env variable as SSL_EMAIL
# echo $SSL_EMAIL
echo "SSL domain set as ${SSL_DOMAIN}"
echo "SSL email set as ${SSL_EMAIL}"
CERT_FILE=/etc/letsencrypt/live/$DOMAIN/cert.pem
if test -f "$CERT_FILE"; then
    exit
fi

wget https://dl.eff.org/certbot-auto
sudo mv certbot-auto /usr/local/bin/certbot-auto
sudo chown root /usr/local/bin/certbot-auto
sudo chmod 0755 /usr/local/bin/certbot-auto
sudo /usr/local/bin/certbot-auto --no-bootstrap
sudo /usr/local/bin/supervisorctl -c /opt/python/etc/supervisord.conf stop httpd
sudo /usr/local/bin/certbot-auto certonly --standalone -m $SSL_EMAIL --agree-tos -d $SSL_DOMAIN -n
sudo /usr/local/bin/supervisorctl -c /opt/python/etc/supervisord.conf start httpd
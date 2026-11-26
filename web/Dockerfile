# STUDENT CONTEXT: S3 | build context ./web
# TO PREPARE / ADAPT: Add your new assets to COPY if you create any.
# EXPECTED CHECK: Check the files served by the image, not only those present on the laptop.
#
# Nginx image designed for a non-root process; the server listens on 8080.
# The provided tag is a starting point: record the digest for traceability.
FROM nginxinc/nginx-unprivileged:stable-alpine
# Compose/Kubernetes configuration: api is an internal DNS name.
COPY default.conf /etc/nginx/conf.d/default.conf
# The files are embedded, unlike the development bind mount.
# TODO S2-S3: complete this list if you add files to the frontend.
COPY index.html app.js styles.css /usr/share/nginx/html/
# Internal port; publishing is defined in Compose or through the Service.
EXPOSE 8080

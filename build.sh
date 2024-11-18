VERSION=$(cat version)
docker build --tag mmcdowell/whc-api:$VERSION .
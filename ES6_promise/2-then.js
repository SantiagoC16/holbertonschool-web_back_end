export default function handleResponseFromAPI(promise) {
  return promise
    .then(() => {
      console.log();
    })
    .catch(() => {
      console.log();
    })
    .finally(() => {
      console.log('Got a response from the API');
    });
}

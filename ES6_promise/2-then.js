export default function handleResponseFromAPI(promise) {
  return promise
    .then((result) => {
      console.log(result);
      return {
        status: 200,
        body: 'success',
      };
    })
    .catch((error) => {
      console.log(error);
    })
    .finally(() => {
      console.log('Got a response from the API');
    });
}

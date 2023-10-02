export default function handleResponseFromAPI(promise) {
  return promise
    .then((result) => {
      result = ({
        status: 200,
        body: 'Success',
      });
      console.log(result);
    })
    .catch((error) => {
      console.log(error);
    })
    .finally(() => {
      console.log('Got a response from the API');
    });
}

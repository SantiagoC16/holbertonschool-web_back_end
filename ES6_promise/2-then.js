export default function handleResponseFromAPI(promise) {
  return promise
    .then((result) => {
      result = 'Got a response from the API'
      console.log(result);
    })
    .catch((error) => {
      console.log(error)
    });
}

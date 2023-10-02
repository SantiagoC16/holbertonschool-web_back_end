export default function getFullResponseFromAPI() {
  return new Promise((resolve) => {
    resolve({
      status: 200,
      body: 'Success',
    });
    console.error('The fake API is not working currently');
  });
}

export default function getFullResponseFromAPI() {
  return new Promise((resolve, reject) => {
    resolve({
      status: 200,
      body: 'Success',
    });
    reject(Error('The fake API is not working currently'));
  });
}

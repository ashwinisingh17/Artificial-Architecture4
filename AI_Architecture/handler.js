async function getData(selectElement) {
    const response = await fetch('http://127.0.0.1:5000/bedroom', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ value: selectElement.value })
    });

    if (response.ok) {
        const data = await response.json();
        console.log(data);
    } else {
        console.error('Failed to execute Python script');
    }
}

export default getData;

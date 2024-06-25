import React, { useEffect, useState } from 'react';

const FortuneHistory = () => {
  const [history, setHistory] = useState([]);

  useEffect(() => {
    const fetchHistory = async () => {
      try {
        const response = await fetch('http://localhost:8000/api/fortune_history'); // Ensure this is the correct URL
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        const data = await response.json();
        console.log('Fetched data:', data); // Log the fetched data
        setHistory(data.history);
      } catch (error) {
        console.error('There was a problem with the fetch operation:', error);
      }
    };

    fetchHistory();
  }, []);

  return (
    <div className="p-4">
      <h1>Fortune History</h1>
      <table className="table-auto w-full">
        <thead>
          <tr>
            <th>Date</th>
            <th>Card</th>
            <th>Fortune</th>
          </tr>
        </thead>
        <tbody>
          {history.map((item, index) => (
            <tr key={index}>
              <td>{new Date(item.timestamp).toLocaleString()}</td>
              <td>{item.card_name}</td>
              <td>{item.fortune_text}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default FortuneHistory;

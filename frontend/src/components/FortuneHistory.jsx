import React, { useState, useEffect } from 'react';

const FortuneHistory = () => {
  const [history, setHistory] = useState([]);

  useEffect(() => {
    fetch('http://localhost:8000/api/fortune_history')
      .then(response => {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        return response.json();
      })
      .then(data => {
        setHistory(data.history);
      })
      .catch(error => {
        console.error('There was a problem with the fetch operation:', error);
      });
  }, []);

  return (
    <div className="p-4">
      <h1>Fortune History</h1>
      <table className="table-auto w-full">
        <thead>
          <tr>
            <th className="px-4 py-2">Card Name</th>
            <th className="px-4 py-2">Fortune Text</th>
            <th className="px-4 py-2">Timestamp</th>
          </tr>
        </thead>
        <tbody>
          {history.map((item, index) => (
            <tr key={index}>
              <td className="border px-4 py-2">{item.card_name}</td>
              <td className="border px-4 py-2">{item.fortune_text}</td>
              <td className="border px-4 py-2">{new Date(item.timestamp).toLocaleString()}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default FortuneHistory;

import React, { useEffect, useState } from 'react';

const FortuneHistory = () => {
  const [history, setHistory] = useState([]);

  useEffect(() => {
    // Fetch the history from the backend API
    fetch('/api/fortune_history')
      .then(response => response.json())
      .then(data => setHistory(data.history));
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
              <td>{item.timestamp}</td>
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

import React, { useState } from 'react';

const DrawCard = () => {
  const [card, setCard] = useState(null);

  const handleDraw = () => {
    console.log('Button clicked, making API call...');
    fetch('http://172.179.16.48:8000/api/draw_card')  // Replace with your backend external IP
      .then(response => {
        console.log('Response received:', response);
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        return response.json();
      })
      .then(data => {
        console.log('API response received:', data);
        setCard(data);
      })
      .catch(error => {
        console.error('There was a problem with the fetch operation:', error);
      });
  };

  return (
    <div className="p-4">
      <h1>Draw Card</h1>
      <div className="flex flex-col items-center">
        {card ? (
          <div className="text-center">
            <img 
              src={`/assets/images/tarot-fronts/${card.card_name}.png`} 
              alt={card.card_name} 
              className="w-1/2"
            />
            <p className="mt-4">{card.fortune_text}</p>
          </div>
        ) : (
          <button onClick={handleDraw} className="bg-blue-500 text-white p-2 rounded">
            Draw a Card
          </button>
        )}
      </div>
    </div>
  );
};

export default DrawCard;

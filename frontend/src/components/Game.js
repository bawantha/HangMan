import React, { useState } from 'react';
import { startNewGame, getGameState, makeGuess } from '../api';

const Game = () => {
  const [gameId, setGameId] = useState(null);
  const [gameState, setGameState] = useState(null);
  const [guess, setGuess] = useState('');
  const [message, setMessage] = useState('');

  const handleStartGame = async () => {
    try {
      const data = await startNewGame();
      setGameId(data.id);
      const state = await getGameState(data.id);
      setGameState(state);
      setMessage('Game started!');
    } catch (error) {
      setMessage('Error starting game.');
    }
  };

  const handleGuess = async () => {
    if (!guess) {
      setMessage('Please enter a letter.');
      return;
    }
    try {
      const response = await makeGuess(gameId, guess);
      setGameState(response.game_state);
      setMessage(response.correct ? 'Correct guess!' : 'Incorrect guess.');
      setGuess('');
    } catch (error) {
      setMessage('Error making guess.');
    }
  };

  return (
    <div style={{ textAlign: 'center', marginTop: '50px' }}>
      <h1>Hangman Game</h1>
      {!gameId && <button onClick={handleStartGame}>Start New Game</button>}
      {gameState && (
        <>
          <h2>Word: {gameState.current_word_state}</h2>
          <p>Incorrect Guesses: {gameState.incorrect_guesses}</p>
          <p>Remaining Guesses: {gameState.remaining_guesses}</p>
          <p>Status: {gameState.state}</p>
          {gameState.state === 'InProgress' && (
            <div>
              <input
                type="text"
                value={guess}
                onChange={(e) => setGuess(e.target.value)}
                maxLength={1}
                placeholder="Enter a letter"
              />
              <button onClick={handleGuess}>Submit Guess</button>
            </div>
          )}
        </>
      )}
      <p>{message}</p>
    </div>
  );
};

export default Game;

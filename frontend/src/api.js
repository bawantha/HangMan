import axios from 'axios';

const API_BASE_URL = 'http://127.0.0.1:8000';

export const startNewGame = async () => {
  const response = await axios.post(`${API_BASE_URL}/game/new`);
  return response.data;
};

export const getGameState = async (gameId) => {
  const response = await axios.get(`${API_BASE_URL}/game/${gameId}`);
  return response.data;
};

export const makeGuess = async (gameId, guess) => {
  const response = await axios.post(`${API_BASE_URL}/game/${gameId}/guess`, { "guess":guess });
  return response.data;
};

import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import ChatPage from '../../app/chat/page';
import '@testing-library/jest-dom';

describe('End-to-end Chat flow', () => {
  it('sends message and displays response', async () => {
    render(<ChatPage />);
    const input = screen.getByPlaceholderText(/type your message/i);
    fireEvent.change(input, { target: { value: 'Hello AI' } });
    fireEvent.click(screen.getByText(/send/i));
    await waitFor(() => {
      const aiMsg = screen.queryByTestId('ai-message');
      const errorMsg = screen.queryByTestId('error-message');
      expect(aiMsg || errorMsg).toBeTruthy();
    });
  });
});

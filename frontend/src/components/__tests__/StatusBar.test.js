import React from 'react';
import { render, screen } from '@testing-library/react';
import StatusBar from '../StatusBar';
import '@testing-library/jest-dom';

describe('StatusBar component', () => {
  it('renders with status text', () => {
    render(<StatusBar status="Ready" />);
    expect(screen.getByText('Ready')).toBeInTheDocument();
  });
});

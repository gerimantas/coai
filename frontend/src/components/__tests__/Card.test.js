import React from 'react';
import { render, screen } from '@testing-library/react';
import Card from '../Card';
import '@testing-library/jest-dom';

describe('Card component', () => {
  it('renders with children', () => {
    render(<Card>Test Card</Card>);
    expect(screen.getByText('Test Card')).toBeInTheDocument();
  });
});

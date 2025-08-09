
# COAI UI Centralized Design and Functionality Plan

## Goal
Create a modern, centrally managed UI so that design and functionality changes are easily applied to all pages.

---

## 1. Color and Style Management
- Create global CSS/Tailwind configuration (`globals.css`, `tailwind.config.js`).
- Define main colors, fonts, border radius, shadow, etc.
- Use CSS variables or Tailwind custom themes.

## 2. UI Component Library
- Create a shared components directory: `Button`, `Card`, `Tab`, `StatusBar`, `Loader`, `Alert`, `Sidebar`, `Toolbar`.
- All pages use only these components.
- Components have clear props (e.g., color, size, variant).

## 3. Layout and Structure
- Create a main `Layout` component (`layout.js`).
- Define common structure: sidebar, toolbar, statusbar, main content.
- All pages use this layout.

## 4. Navigation
- Create a `Tab` or `NavBar` component with active tab highlighting.
- Navigation style and functionality managed in one component.

## 5. Dark/Light Mode
- Support dark/light mode via Tailwind or CSS variables.
- Mode switching affects all components.

## 6. Responsiveness
- All components must be responsive.
- Layout automatically adapts to screen size.

## 7. Centralized Functionality
- Status, notifications, loaders, errors are shown via shared components.
- API calls, user data, project info are managed via shared context (`React Context` or `zustand` store).

## 8. Icons and Visuals
- Use a shared icon library (e.g., Heroicons, FontAwesome).
- Icons and visuals integrated into components via props.

## 9. Documentation
- Document UI component usage, props, and style change principles in README or a separate UI guideline file.

---

## Actions
1. Create and configure global style file and Tailwind theme.
	- Ensure globals.css exists and is imported in _app.js/layout.js.
	- Define main colors, fonts, border radius, shadows, and CSS variables for dark/light mode in globals.css and tailwind.config.js.
	- Use Tailwind dark theme template as a reference for color palette and component styling.
	- Analyze and refactor chat page styles and components to use centralized theme and global styles.
	- Recommendation: Chat page should use Tailwind dark theme, consistent spacing, and shared UI components (Button, Card, etc.).
2. Refactor existing pages to use shared UI components.
3. Create main layout component and apply to all pages.
4. Create and use shared navigation, status, notification components.
5. Document UI change principles.

---

## Recommended UI Folder and File Structure

```
frontend/
	src/
		app/
			globals.css         # Global styles and CSS variables
			layout.js           # Main Layout component
			page.js             # Main page
			chat/page.js        # Chat page
			...                 # Other pages
		components/
			Button.js           # Shared button component
			Card.js             # Shared card component
			Tab.js              # Navigation tab component
			StatusBar.js        # Status bar
			Sidebar.js          # Sidebar
			Toolbar.js          # Toolbar
			Loader.js           # Loader component
			Alert.js            # Notification/alert component
			...                 # Other shared components
```

All pages and UI elements use only these shared components and global styles. Any design or functionality changes are applied centrally and instantly across the entire UI.

## Result
Any design or functionality changes are applied to the entire UI quickly and centrally.

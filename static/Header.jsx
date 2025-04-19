import React from 'react';

const Header = () => {
  return (
    <header className="fixed top-0 left-0 right-0 bg-white border-b border-gray-200 px-4 sm:px-6 h-14 sm:h-16 flex justify-between items-center z-50">
      {/* Left side - Logo and Brand */}
      <div className="flex items-center">
        <svg
          className="w-6 h-6 text-yellow-500"
          fill="currentColor"
          viewBox="0 0 20 20"
          xmlns="http://www.w3.org/2000/svg"
        >
          <path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z" />
        </svg>
        <span className="text-lg font-semibold text-gray-900 ml-2">
          Prestige Ceremonials
        </span>
      </div>

      {/* Right side - Navigation */}
      <div className="flex items-center space-x-4">
        {/* Navigation Links - Hidden on mobile */}
        <nav className="hidden md:flex items-center space-x-6">
          <a href="/services" className="text-base text-gray-800 hover:text-gray-900 underline">
            Services
          </a>
          <a href="/portfolio" className="text-base text-gray-800 hover:text-gray-900 underline">
            Portfolio
          </a>
          <a href="/about" className="text-base text-gray-800 hover:text-gray-900 underline">
            About
          </a>
          <a href="/contact" className="text-base text-gray-800 hover:text-gray-900 underline">
            Contact
          </a>
        </nav>

        {/* Search Button */}
        <button className="w-10 h-10 flex items-center justify-center rounded-lg bg-gray-100 hover:bg-gray-200">
          <svg
            className="w-5 h-5 text-gray-600"
            fill="none"
            stroke="currentColor"
            viewBox="0 0 24 24"
            xmlns="http://www.w3.org/2000/svg"
          >
            <path
              strokeLinecap="round"
              strokeLinejoin="round"
              strokeWidth={2}
              d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"
            />
          </svg>
        </button>

        {/* Hamburger Menu - Hidden on desktop */}
        <button className="md:hidden w-10 h-10 flex items-center justify-center rounded-lg bg-gray-100 hover:bg-gray-200">
          <svg
            className="w-6 h-6 text-gray-600"
            fill="none"
            stroke="currentColor"
            viewBox="0 0 24 24"
            xmlns="http://www.w3.org/2000/svg"
          >
            <path
              strokeLinecap="round"
              strokeLinejoin="round"
              strokeWidth={2}
              d="M4 6h16M4 12h16M4 18h16"
            />
          </svg>
        </button>

        {/* Avatar */}
        <div className="w-9 h-9 rounded-full ring-2 ring-yellow-500 overflow-hidden">
          <img
            src="/static/images/avatar-placeholder.jpg"
            alt="User avatar"
            className="w-full h-full object-cover"
          />
        </div>
      </div>
    </header>
  );
};

export default Header; 
// .eslintrc.js
module.exports = {
    root: true, // Important for monorepos or multi-package projects
    env: {
        browser: true,
        es2021: true,
        node: true, // Add node environment if needed
    },
    extends: [
        'eslint:recommended',
        'plugin:react/recommended',
        'plugin:react-hooks/recommended',
        'plugin:prettier/recommended', // Make sure this is always the last configuration in the extends array.
    ],
    parserOptions: {
        ecmaFeatures: {
            jsx: true,
        },
        ecmaVersion: 'latest',
        sourceType: 'module',
    },
    plugins: ['react', 'react-hooks', 'prettier'],
    rules: {
        // Your custom rules here
    },
    overrides: [ // This is for backend
        {
            files: ["backend/**/*.py"],
            plugins: ["python"],
            extends: ["plugin:python/recommended"],
            parser: "python-eslint-parser",
            parserOptions: {
                project: "./backend/pyproject.toml",
            },
        },
    ],
};
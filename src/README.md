# Auto-generate profile

Run the following shell script in the `scr` directory to generate an `index.html` file. Replace it with the `index` file in the home directory.

```python
python3 populate.py template.html profile.json
```

Remember to replace corresponding images before publishing.

## Attention

1. `title_2` can be an empty string.
2. `professional.skills` should not be more than 6. 6 is the maximum.
3. `professional.projects` should not be more than 4. Otherwise it is too long.

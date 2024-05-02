FROM apache/superset
ENV SUPERSET_SECRET_KEY=xQXsITfo74ALPPAcC6i5yRiQZOFjULAv0QgPEUA57k0jl0RZ70HKSPJP
RUN pip install Flask-OAuthlib Authlib mysqlclient  
COPY superset_config.py /app/pythonpath/superset_config.py

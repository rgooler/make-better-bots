FROM python:3.9

# Install dependencies
RUN apt-get update && apt-get install -y \
    wget \
    gnupg \
    xvfb \
    fluxbox \
    x11vnc \
    net-tools \
    git \
    && rm -rf /var/lib/apt/lists/*

# Install noVNC from source
RUN git clone https://github.com/novnc/noVNC.git /usr/share/novnc \
    && git clone https://github.com/novnc/websockify /usr/share/novnc/utils/websockify

# Install Chrome
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list \
    && apt-get update \
    && apt-get install -y google-chrome-stable \
    && rm -rf /var/lib/apt/lists/* \
    && mkdir -p /etc/opt/chrome/policies/managed /etc/opt/chrome/policies/recommended

COPY chrome/recommended_policies.json /etc/opt/chrome/policies/recommended/
COPY chrome/managed_policies.json /etc/opt/chrome/policies/managed/

# Install ChromeDriver
RUN google-chrome-stable --version | cut -d' ' -f 3 > /tmp/chrome_version\
    && cat /tmp/chrome_version \
    && wget -q https://storage.googleapis.com/chrome-for-testing-public/$(cat /tmp/chrome_version)/linux64/chromedriver-linux64.zip \
    && unzip chromedriver-linux64.zip \
    && mv chromedriver-linux64/chromedriver /usr/local/bin/ \
    && rm chromedriver-linux64.zip

# Set up noVNC
RUN ln -s /usr/share/novnc/vnc.html /usr/share/novnc/index.html

# Create working directory
WORKDIR /app

# Copy your Python script
COPY app/* .

# Install Python packages
RUN pip install -r requirements.txt

# Copy startup script
RUN chmod +x /app/start.sh

# Expose noVNC port
EXPOSE 5900 6900

CMD ["/app/start.sh"]
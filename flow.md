# Flow

Flow consist of implementation plan for softledger uploads based on the data in database(we are using DBql.)

## Table of Content

- Data Source
- Actions
- Flow

### Data Source

Currently, Coinbase Custody data needs to be imported from cb into softledger and google sheets.

### Actions

Following step are involved in doing so,


### Flow Implementation

There are appropriate scripts in py-softledger anything realted to softledger and data ETL scripts are in respective client repo's.

```mermaid
graph TD

    subgraph Overview

    1[Exchange/blockchain data] -->|step: 1| 2[(DB)];
    2[(DB)] -->|step: 2| 3[Google Sheets];
    3[Google Sheets] -.->|step: 3| 5[Data SignOff];
    5[/Data SignOff/] -.-> 4[Softledger];
    2[(DB)] -->|step: 4| 4[Softledger];

    end

    subgraph Step 1

    1.1[Gnerate API Header] --> 1.2[Dwnload raw data];
    1.2[get raw data] --> 1.3[DB];
    1.2[get raw data] -.-> 1.4[GS formatted  tx];
    1.4[GS formatted  tx]--> 1.3[DB];

    end

```
